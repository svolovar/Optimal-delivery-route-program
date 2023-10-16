# HashTable class using chaining.
# Citing source:  zybooks 7.8: chaining hash table

class MakePackageTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=40):
        # initialize the hash table with empty bucket list entries.
        self.list = []
        for i in range(initial_capacity):
            self.list.append([])

    # Inserts a new item into the hash table.
    # The complexity of this function depends on the number of elements in the hash table. On average, the complexity is
    # O(1)
    def add_package(self, key, item):  # does both insert and update
        # get the bucket list where this package will go.
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        # update key if it is already in the bucket
        for keyValue in bucket_list:
            if keyValue[0] == key:
                keyValue[1] = item
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def lookup_package(self, key):
        # The complexity of this function depends on the number of elements in the hash table. On average, the
        # complexity is O(1)
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        # search for the key in the bucket list
        for pair in bucket_list:
            if key == pair[0]:
                return pair[1]  # value
        return None

    # Removes an item with matching key from the hash table.
    def remove_package(self, key):
        # The complexity of this function depends on the number of elements in the hash table. On average,
        # the complexity is O(1)
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])
