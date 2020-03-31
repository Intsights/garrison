import rocksdb
import rocksdb.errors
import os


class RocksDBQueue:
    def __init__(
        self,
        database_path,
        database_name,
    ):
        database_path = f'{database_path}/queues/{database_name}'
        os.makedirs(
            name=database_path,
            exist_ok=True,
        )

        rocksdb_options = rocksdb.Options()
        rocksdb_options.create_if_missing = True
        rocksdb_options.max_open_files = 300000
        rocksdb_options.write_buffer_size = 67108864
        rocksdb_options.max_write_buffer_number = 3
        rocksdb_options.target_file_size_base = 67108864
        rocksdb_options.compression = rocksdb.CompressionType.no_compression
        rocksdb_options.table_factory = rocksdb.BlockBasedTableFactory(
            filter_policy=rocksdb.BloomFilterPolicy(
                bits_per_key=10,
            ),
        )

        self.database_obj = rocksdb.DB(
            db_name=database_path,
            opts=rocksdb_options,
        )

        self.database_obj.compact_range(
            begin=None,
            end=None,
        )
        self.database_iterator = self.database_obj.iteritems()

        self.database_iterator.seek_to_last()
        try:
            key, value = next(self.database_iterator)
            self.last_key = key
        except StopIteration:
            self.last_key = b''

        self.database_iterator.seek_to_first()
        try:
            key, value = next(self.database_iterator)
            self.first_key = key
            self.database_iterator.seek(self.first_key)
        except StopIteration:
            self.first_key = b''

        self.db_was_changed_recently = False

    def queue_pop(
        self,
        number_of_items,
    ):
        items = []
        keys = []

        if self.db_was_changed_recently:
            self.db_was_changed_recently = False
            self.database_iterator = self.database_obj.iteritems()
            self.database_iterator.seek(self.first_key)

        items_fetched = 0
        for key, value in self.database_iterator:
            items.append(value)
            keys.append(key)

            items_fetched += 1
            if items_fetched == number_of_items:
                break

        if keys:
            database_write_batch = rocksdb.WriteBatch()
            for key in keys:
                database_write_batch.delete(key)

            self.database_obj.write(
                batch=database_write_batch,
                disable_wal=True,
            )

            try:
                key, value = next(self.database_iterator)
                self.first_key = key
                self.database_iterator.seek(key)
            except StopIteration:
                self.first_key = b''
                self.last_key = b''
                self.database_obj.compact_range(
                    begin=None,
                    end=None,
                )
        else:
            self.first_key = b''
            self.last_key = b''
            self.database_obj.compact_range(
                begin=None,
                end=None,
            )

        return items

    def queue_push(
        self,
        items,
        priority,
    ):
        if not items:
            return False

        if priority == 'NORMAL':
            if self.last_key != b'':
                next_item_number = int(self.last_key) + 1
            else:
                next_item_number = int((10 ** 16) / 2)
            factor = 1
        elif priority == 'HIGH':
            if self.first_key != b'':
                next_item_number = int(self.first_key) - 1
            else:
                next_item_number = int((10 ** 16) / 2) - 1
            factor = -1
            items = reversed(items)
        else:
            raise Exception(f'unknown priority level: {priority}')

        database_write_batch = rocksdb.WriteBatch()
        for item in items:
            next_item_key = str(next_item_number).rjust(20, '0').encode('utf-8')
            database_write_batch.put(
                next_item_key,
                item,
            )
            next_item_number += factor

        self.database_obj.write(
            batch=database_write_batch,
            disable_wal=True,
        )

        if factor == 1:
            self.last_key = next_item_key
            if self.first_key == b'':
                self.first_key = str(int((10 ** 16) / 2)).rjust(20, '0').encode('utf-8')
        else:
            self.first_key = next_item_key
            if self.last_key == b'':
                self.last_key = str(int((10 ** 16) / 2) - 1).rjust(20, '0').encode('utf-8')

        self.db_was_changed_recently = True

        return True

    def queue_delete(
        self,
    ):
        database_keys_iterator = self.database_obj.iterkeys()
        database_keys_iterator.seek_to_first()

        while True:
            database_write_batch = rocksdb.WriteBatch()

            num_of_keys = 0
            num_of_keys_per_chunk = 5000

            for key in database_keys_iterator:
                database_write_batch.delete(key)

                num_of_keys += 1
                if num_of_keys == num_of_keys_per_chunk:
                    break

            self.database_obj.write(
                batch=database_write_batch,
                sync=True,
            )

            if num_of_keys != num_of_keys_per_chunk:
                break

        self.database_obj.compact_range(
            begin=None,
            end=None,
        )
        self.first_key = b''
        self.last_key = b''
        self.db_was_changed_recently = True

        return True

    def queue_length(
        self,
    ):
        if self.first_key == b'' or self.last_key == b'':
            return 0
        else:
            first_key_number = int(self.first_key)
            last_key_number = int(self.last_key)

            return last_key_number - first_key_number + 1


class RocksDBKeys:
    def __init__(
        self,
        database_path,
        database_name,
    ):
        database_path = f'{database_path}/keys/{database_name}'
        os.makedirs(
            name=database_path,
            exist_ok=True,
        )

        rocksdb_options = rocksdb.Options()
        rocksdb_options.create_if_missing = True
        rocksdb_options.max_open_files = 300000
        rocksdb_options.write_buffer_size = 67108864
        rocksdb_options.max_write_buffer_number = 3
        rocksdb_options.target_file_size_base = 67108864
        rocksdb_options.compression = rocksdb.CompressionType.no_compression
        rocksdb_options.table_factory = rocksdb.BlockBasedTableFactory(
            filter_policy=rocksdb.BloomFilterPolicy(
                bits_per_key=10,
            ),
        )

        self.database_obj = rocksdb.DB(
            db_name=database_path,
            opts=rocksdb_options,
        )

        self.database_obj.compact_range(
            begin=None,
            end=None,
        )

    def key_get(
        self,
        key,
    ):
        value = self.database_obj.get(
            key=key,
        )

        return value

    def key_set(
        self,
        key,
        value,
    ):
        current_key = self.database_obj.get(
            key=key,
        )
        is_new_key = current_key is None

        self.database_obj.put(
            key=key,
            value=value,
            sync=True,
        )

        return is_new_key

    def key_delete(
        self,
        key,
    ):
        current_key = self.database_obj.get(
            key=key,
        )
        key_does_not_exist = current_key is None
        if key_does_not_exist:
            return False

        self.database_obj.delete(
            key=key,
            sync=True,
        )

        return True
