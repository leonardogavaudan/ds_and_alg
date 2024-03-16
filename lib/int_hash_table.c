#include <stdint.h>
#include <stdlib.h>

#define HASH_TABLE_MAX_SIZE 1 << 16
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

HashTable *createHashTable(uint16_t maxSize) {
  HashTable *hashTable = malloc(sizeof(HashTable));
  if (hashTable == NULL) {
    return NULL;
  }

  hashTable->size = 0;
  hashTable->maxSize = maxSize;
  hashTable->hashItems = malloc(maxSize * sizeof(HashItem *));

  for (int i = 0; i < maxSize; i++) {
    hashTable->hashItems[i] = NULL;
  }

  return hashTable;
}

int16_t hash(HashTable *hashTable, int16_t key) {
  return key % hashTable->maxSize;
}

HashTable *resizeHashTable(HashTable *hashTable) {
  HashTable *newHashTable = createHashTable(hashTable->maxSize * 2);
  if (newHashTable == NULL) {
    return NULL;
  }
  for (int i = 0; i < hashTable->maxSize; i++) {
    newHashTable->hashItems[i] = hashTable->hashItems[i];
  }

  return newHashTable;
}

void setHashItem(HashTable *hashTable, int16_t key, int32_t value) {
  if (((float)hashTable->size / hashTable->maxSize) > MAX_LOAD_FACTOR) {
    HashTable *newHashTable = resizeHashTable(hashTable);
    if (newHashTable == NULL) {
      return;
    }

    hashTable = newHashTable;
  }

  int16_t hashResult = hash(hashTable, key);
  int initialHashResult = hashResult;
  do {
    hashResult = (hashResult + 1) % hashTable->maxSize;
  } while (hashTable->hashItems[hashResult] != NULL &&
           hashResult != initialHashResult &&
           hashTable->hashItems[hashResult]->key != key);

  HashItem *hashItem = malloc(sizeof(HashItem));
  hashTable->hashItems[hashResult] = hashItem;
  hashTable->size++;
}

int32_t getHashItemValue(HashTable *hashTable, int16_t key) {
  int16_t hashResult = hash(hashTable, key);
  int16_t initialHashResult = hashResult;
  if (hashTable->hashItems[hashResult] == NULL) {
    return -1;
  }

  do {
    if (hashTable->hashItems[hashResult]->key == key) {
      return hashTable->hashItems[hashResult]->value;
    }
    hashResult = (hashResult + 1) % hashTable->maxSize;
  } while (hashTable->hashItems[hashResult] != NULL &&
           hashResult != initialHashResult);

  return -1;
}
