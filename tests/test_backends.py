import unittest
import tempfile

import garrison


class RocksDBBackendTestCase(
    unittest.TestCase,
):
    def test_keys(
        self,
    ):
        test_key_name = b'test_key_name'
        test_key_value = b'test_key_value'

        with tempfile.TemporaryDirectory() as tmpdir:
            backend_keys = garrison.backends.rocksdb.RocksDBKeys(
                database_path=tmpdir,
                database_name='test_keys',
            )

            key_was_deleted = backend_keys.key_delete(
                key=test_key_name,
            )
            self.assertFalse(
                expr=key_was_deleted,
            )

            key_value = backend_keys.key_get(
                key=test_key_name,
            )
            self.assertEqual(
                first=key_value,
                second=None,
            )

            is_new_key = backend_keys.key_set(
                key=test_key_name,
                value=test_key_value,
            )
            self.assertTrue(
                expr=is_new_key,
            )
            key_value = backend_keys.key_get(
                key=test_key_name,
            )
            self.assertEqual(
                first=key_value,
                second=test_key_value,
            )

            key_was_deleted = backend_keys.key_delete(
                key=test_key_name,
            )
            self.assertTrue(
                expr=key_was_deleted,
            )

            key_value = backend_keys.key_get(
                key=test_key_name,
            )
            self.assertEqual(
                first=key_value,
                second=None,
            )

    def test_queue_scenario_one(
        self,
    ):
        with tempfile.TemporaryDirectory() as tmpdir:
            backend_queue = garrison.backends.rocksdb.RocksDBQueue(
                database_path=tmpdir,
                database_name='test_queue',
            )

            backend_queue.queue_delete()

            queue_length = backend_queue.queue_length()
            self.assertEqual(
                first=queue_length,
                second=0,
            )

            backend_queue.queue_push(
                items=[
                    b'1',
                ],
                priority='NORMAL',
            )

            queue_length = backend_queue.queue_length()
            self.assertEqual(
                first=queue_length,
                second=1,
            )

            items = backend_queue.queue_pop(
                number_of_items=1,
            )
            self.assertEqual(
                first=items,
                second=[
                    b'1',
                ],
            )

            queue_length = backend_queue.queue_length()
            self.assertEqual(
                first=queue_length,
                second=0,
            )

            backend_queue.queue_push(
                items=[
                    b'1',
                ],
                priority='NORMAL',
            )

            queue_length = backend_queue.queue_length()
            self.assertEqual(
                first=queue_length,
                second=1,
            )

            items = backend_queue.queue_pop(
                number_of_items=1,
            )
            self.assertEqual(
                first=items,
                second=[
                    b'1',
                ],
            )

            queue_length = backend_queue.queue_length()
            self.assertEqual(
                first=queue_length,
                second=0,
            )

    def test_queue_scenario_two(
        self,
    ):
        with tempfile.TemporaryDirectory() as tmpdir:
            test_items = [
                b'1',
                b'2',
                b'3',
                b'4',
                b'5',
            ] * 1000

            backend_queue = garrison.backends.rocksdb.RocksDBQueue(
                database_path=tmpdir,
                database_name='test_queue',
            )

            backend_queue.queue_delete()

            for i in range(10):
                queue_length = backend_queue.queue_length()
                self.assertEqual(
                    first=queue_length,
                    second=0,
                )

                backend_queue.queue_push(
                    items=test_items,
                    priority='NORMAL',
                )

                queue_length = backend_queue.queue_length()
                self.assertEqual(
                    first=queue_length,
                    second=len(test_items),
                )

                popped_items = backend_queue.queue_pop(
                    number_of_items=1,
                )
                self.assertEqual(
                    first=popped_items,
                    second=[test_items[0]],
                )
                queue_length = backend_queue.queue_length()
                self.assertEqual(
                    first=queue_length,
                    second=len(test_items) - 1,
                )

                popped_items = backend_queue.queue_pop(
                    number_of_items=4999,
                )
                self.assertEqual(
                    first=popped_items,
                    second=test_items[1:],
                )

                queue_length = backend_queue.queue_length()
                self.assertEqual(
                    first=queue_length,
                    second=0,
                )

                popped_items = backend_queue.queue_pop(
                    number_of_items=100,
                )
                self.assertEqual(
                    first=popped_items,
                    second=[],
                )

                queue_length = backend_queue.queue_length()
                self.assertEqual(
                    first=queue_length,
                    second=0,
                )

    def test_queue_scenario_three(
        self,
    ):
        with tempfile.TemporaryDirectory() as tmpdir:
            test_items_normal = [
                b'1',
            ] * 1000
            test_items_high = [
                b'2',
            ] * 1000

            backend_queue = garrison.backends.rocksdb.RocksDBQueue(
                database_path=tmpdir,
                database_name='test_queue',
            )

            backend_queue.queue_delete()

            for i in range(10):
                queue_length = backend_queue.queue_length()
                self.assertEqual(
                    first=queue_length,
                    second=0,
                )

                backend_queue.queue_push(
                    items=test_items_normal,
                    priority='NORMAL',
                )
                backend_queue.queue_push(
                    items=test_items_high,
                    priority='HIGH',
                )

                queue_length = backend_queue.queue_length()
                self.assertEqual(
                    first=queue_length,
                    second=len(test_items_normal) + len(test_items_high),
                )

                popped_items = backend_queue.queue_pop(
                    number_of_items=len(test_items_normal) + len(test_items_high) + 100,
                )
                self.assertEqual(
                    first=popped_items,
                    second=test_items_high + test_items_normal,
                )

                queue_length = backend_queue.queue_length()
                self.assertEqual(
                    first=queue_length,
                    second=0,
                )

                backend_queue.queue_push(
                    items=test_items_high,
                    priority='HIGH',
                )
                backend_queue.queue_push(
                    items=test_items_normal,
                    priority='NORMAL',
                )

                queue_length = backend_queue.queue_length()
                self.assertEqual(
                    first=queue_length,
                    second=len(test_items_normal) + len(test_items_high),
                )

                popped_items = backend_queue.queue_pop(
                    number_of_items=len(test_items_normal) + len(test_items_high) + 100,
                )
                self.assertEqual(
                    first=popped_items,
                    second=test_items_high + test_items_normal,
                )

                queue_length = backend_queue.queue_length()
                self.assertEqual(
                    first=queue_length,
                    second=0,
                )

    def test_queue_scenario_four(
        self,
    ):
        with tempfile.TemporaryDirectory() as tmpdir:
            backend_queue = garrison.backends.rocksdb.RocksDBQueue(
                database_path=tmpdir,
                database_name='test_queue',
            )

            backend_queue.queue_delete()

            backend_queue.queue_push(
                items=[
                    b'1',
                ] * 1000,
                priority='NORMAL',
            )

            queue_length = backend_queue.queue_length()
            self.assertEqual(
                first=queue_length,
                second=1000,
            )

            del backend_queue

            backend_queue = garrison.backends.rocksdb.RocksDBQueue(
                database_path=tmpdir,
                database_name='test_queue',
            )

            queue_length = backend_queue.queue_length()
            self.assertEqual(
                first=queue_length,
                second=1000,
            )

            popped_items = backend_queue.queue_pop(
                number_of_items=1000,
            )
            self.assertEqual(
                first=popped_items,
                second=[
                    b'1',
                ] * 1000,
            )

    def test_queue_scenario_five(
        self,
    ):
        with tempfile.TemporaryDirectory() as tmpdir:
            backend_queue = garrison.backends.rocksdb.RocksDBQueue(
                database_path=tmpdir,
                database_name='test_queue',
            )

            backend_queue.queue_delete()

            backend_queue.queue_push(
                items=[
                    b'1',
                ] * 5,
                priority='NORMAL',
            )

            backend_queue.queue_delete()

            queue_length = backend_queue.queue_length()
            self.assertEqual(
                first=queue_length,
                second=0,
            )

            popped_items = backend_queue.queue_pop(
                number_of_items=1000,
            )
            self.assertEqual(
                first=popped_items,
                second=[],
            )

            del backend_queue
