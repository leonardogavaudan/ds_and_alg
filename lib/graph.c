#include <stdlib.h>

typedef struct node {
  int vertex;
  struct Node *next;
} Node;

typedef struct graph {
  int verticesCount;
  Node **adjacencyList;
} Graph;

Graph *createGraph(int verticesCount) {
  Graph *graph = malloc(sizeof(Graph));
  graph->verticesCount = verticesCount;
  Node **adjacencyList = malloc(verticesCount * sizeof(Node *));

  for (int i = 0; i < verticesCount; i++) {
    adjacencyList[i] = NULL;
  }

  graph->adjacencyList = adjacencyList;

  return graph;
}

void addEdge(Graph *graph, int sourceVertex, int destinationVertex) {}
