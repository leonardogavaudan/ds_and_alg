#include <stdint.h>

typedef struct hashItem {
  int key;
  int value;
} HashItem;

typedef struct hashTable {
  int size;
  int maxSize;
  HashItem **hashItems;
} HashTable;

void freeHashTable(HashTable *hashTable);

HashTable *createHashTable(int size);

int setHashItem(HashTable *hashTable, int key, int value);

HashItem *getHashItem(HashTable *hashTable, int key);
