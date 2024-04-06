#include <stdlib.h>

#define MAX_LOAD_FACTOR 0.75

typedef struct hashItem {
  int key;
  int value;
} HashItem;

typedef struct hashTable {
  int size;
  int maxSize;
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

HashTable *createHashTable(int size) {
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

int getHash(HashTable *hashTable, int key) { return key % hashTable->maxSize; }

int getHashWithoutConflict(HashTable *hashTable, int hash) {
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

    int hash = getHash(newHashTable, hashTable->hashItems[i]->key);
    int hashWithoutConflict = getHashWithoutConflict(newHashTable, hash);
    if (hashWithoutConflict == -1) {
      return NULL;
    }

    newHashTable->hashItems[hashWithoutConflict] = hashTable->hashItems[i];
  }

  freeHashTableWithoutItems(hashTable);
  return newHashTable;
}

int setHashItemWithoutResizing(HashTable *hashTable, int key, int value) {
  int hash = getHash(hashTable, key);

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

int setHashItem(HashTable *hashTable, int key, int value) {
  if (((float)hashTable->size / hashTable->maxSize) > MAX_LOAD_FACTOR) {
    HashTable *newHashTable = resizeHashTable(hashTable);
    if (newHashTable == NULL) {
      return -1;
    }

    hashTable = newHashTable;
  }

  return setHashItemWithoutResizing(hashTable, key, value);
}

HashItem *getHashItemByKey(HashTable *hashTable, int key) {
  int hash = getHash(hashTable, key);
  int initialHash = hash;

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
