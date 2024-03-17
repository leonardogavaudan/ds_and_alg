#include <stdint.h>
#include <stdlib.h>

#define MAX_LOAD_FACTOR 0.75

typedef struct hashItem {
  int16_t key;
  int32_t value;
} HashItem;

typedef struct hashTable {
  uint16_t size;
  uint16_t maxSize;
  HashItem **hashItems;
} HashTable;

void freeHashTableItems(HashTable *hashTable) {
  for (int i = 0; i < hashTable->maxSize; i++) {
    if (hashTable->hashItems[i] != NULL) {
      free(hashTable->hashItems[i]);
    }
  }
}

void freeHashTableWithoutItems(HashTable *hashTable) {
  free(hashTable->hashItems);
  free(hashTable);
}

void freeHashTable(HashTable *hashTable) {
  freeHashTableItems(hashTable);
  freeHashTableWithoutItems(hashTable);
}

HashTable *createHashTable(uint16_t size) {
  HashTable *hashTable = malloc(sizeof(HashTable));
  if (hashTable == NULL) {
    return NULL;
  }

  hashTable->size = 0;
  hashTable->maxSize = size;
  hashTable->hashItems = malloc(size * sizeof(HashItem *));
  if (hashTable->hashItems == NULL) {
    freeHashTableWithoutItems(hashTable);
    return NULL;
  }

  for (int i = 0; i < size; i++) {
    hashTable->hashItems[i] = NULL;
  }

  return hashTable;
}

int16_t getHash(HashTable *hashTable, int16_t key) {
  return key % hashTable->maxSize;
}

int16_t getHashWithoutConflict(HashTable *hashTable, int16_t hash) {
  int initialHash = hash;

  while (hashTable->hashItems[hash] != NULL) {
    hash = (hash + 1) % hashTable->maxSize;
    if (hash == initialHash) {
      return -1;
    }
  }

  return hash;
}

HashTable *resizeHashTable(HashTable *hashTable) {
  HashTable *newHashTable = createHashTable(hashTable->maxSize * 2);
  if (newHashTable == NULL) {
    return NULL;
  }

  for (int i = 0; i < hashTable->maxSize; i++) {
    if (hashTable->hashItems[i] == NULL) {
      continue;
    }

    int16_t hash = getHash(newHashTable, hashTable->hashItems[i]->key);
    int16_t hashWithoutConflict = getHashWithoutConflict(newHashTable, hash);
    if (hashWithoutConflict == -1) {
      return NULL;
    }

    newHashTable->hashItems[hashWithoutConflict] = hashTable->hashItems[i];
  }

  freeHashTableWithoutItems(hashTable);
  return newHashTable;
}

int8_t setHashItemWithoutResizing(HashTable *hashTable, int16_t key,
                                  int32_t value) {
  int16_t hash = getHash(hashTable, key);

  int initialHash = hash;
  while (hashTable->hashItems[hash] != NULL &&
         hashTable->hashItems[hash]->key != key) {
    hash = (hash + 1) % hashTable->maxSize;
    if (hash == initialHash) {
      return -1;
    }
  };

  if (hashTable->hashItems[hash] == NULL) {
    HashItem *newHashItem = malloc(sizeof(HashItem));
    if (newHashItem == NULL) {
      return -1;
    }
    hashTable->hashItems[hash] = newHashItem;
    hashTable->size++;
  }

  hashTable->hashItems[hash]->key = key;
  hashTable->hashItems[hash]->value = value;

  return 1;
}

int8_t setHashItem(HashTable *hashTable, int16_t key, int32_t value) {
  if (((float)hashTable->size / hashTable->maxSize) > MAX_LOAD_FACTOR) {
    HashTable *newHashTable = resizeHashTable(hashTable);
    if (newHashTable == NULL) {
      return -1;
    }

    hashTable = newHashTable;
  }

  return setHashItemWithoutResizing(hashTable, key, value);
}

HashItem *getHashItemByKey(HashTable *hashTable, int16_t key) {
  int16_t hash = getHash(hashTable, key);
  int16_t initialHash = hash;

  while (hashTable->hashItems[hash] != NULL) {
    if (hashTable->hashItems[hash]->key == key) {
      return hashTable->hashItems[hash];
    }

    hash = (hash + 1) % hashTable->maxSize;

    if (hash == initialHash) {
      return NULL;
    }
  }

  return NULL;
}
