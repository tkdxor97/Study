# 자료구조 (Data Structure)

- 상황과 문맥에 맞게 데이터를 담을 수 있는 적절한 구조를 말하며, 데이터에 편리하게 접근하고 조작하기 위한 방법이다.
- 자료 구조는 크게 단순 구조와 비단순 구조로 나뉜다. 
    - 단순구조는 프로그래밍에서 사용되는 기본 데이터 타입을 의미하며, ex) Character, Integer ... 
    - 비단순 구조는 단순한 데이터를 저장하는 구조가 아니라 여러 데이터를 목적에 맞게 효과적으로 저장하는 자료구조 이며, 선형구조와 비선형 구조로 나뉜다.
        - `선형구조 : 저장되는 자료의 전후 관계가 1대1(List, Stack, Queue)`
        - `비선형구조 : 데이터 항목 사이의 관계가 1:n 도는 n:m(Graph, Tree)`

## 배열(Array)
---
`가장 기본적인 자료구조로 동일한 자료형의 데이터를 일렬로 나열한 자료구조`
- 데이터 접근이 용이.
- 데이터 삽입/삭제가 어려움.
    > 중간에 삽입시 뒤로 1칸씩 밀어주어야 함. O(n)
- 구조가 간단하여 프로그램 작성이 쉬움.

## 연결리스트(Linked List)
---
`각 노드가 데이터와 포인터를 가지고 일렬로 연결되어있는 방식으로 데이터를 저장하는 자료구조.`
- 배열과 반대되는 특징을 가짐.
- 데이터의 접근이 느림.
- 데이터의 삽입/삭제가 용이.
- 포인터를 위한 추가 공간 필요, 프로그램 작성이 어려움.

## 스택(Stack)
---
`삽입연산, 삭제 연산이 한 방향에서 이루어지는 선형 자료구조.`
- 한 방향에서 삽입과 삭제가 이루어지기 때문에 후입선출(LIFO, Last In First out)구조를 갖음.
- 스택에 데이터가 삽입될 위치를 Top, 삽입을 Push, 삭제 Pop이라고 한다.

## 큐(Queue)
---
`삽입 연산과 삭제 연산이 서로 다른 방향에서 이루어지는 선형 자료구조`
- 한 방향에서는 삽입이, 반대 방향에서는 삭제가 이루어지기 때문에 먼저 삽입된 데이터가 먼저 삭제되는 선입선출(FIFO, First In First Out) 구조를 가진다.
- 데이터가 삭제될 위치를 Front / Head , 마지막 데이터가 삽입된 위치를 Rear / Tail이라 부른다.
- 양방향에서 삽입연산과 삭제 연산이 모두 이루어지는 큐를 덱(deque)라고 한다.

**원형 큐**
원형 큐는 선형 큐의 문제점을 보완하기 위한 자료구조이다. rear가 가르키는 포인터가 배열의 마지막 인덱스를 가리키고 있을 때, 앞쪽에서 Dequeue로 발생한 배열의 빈 공간을 활용 할 수가 없다. 원형큐는 포인터 증가 방식이 `(rear + 1) % size` 이기 때문에 배열의 첫 인덱스부터 다시 데이터 삽입이 가능해진다.


## 트리 (Tree)
---
1개 이상의 노드를 갖는 집합의 자료구조. 자료들 사이의 계층적 관계를 나타내는데 사용하는 자료구조로 부모-자식 관계로 표현된다. 
- 루트(root) 노드가 존재한다.
- 트리의 부분트리(Sub Tree) 또한 트리 구조를 따른다.
- 순환(cycle)이 있으면 안된다.

- Node(노드) : 트리를 구성하고 있는 원소 그 자체를 말한다.
- Edge(간선) : 노드와 노드사이를 연결하고 있는 선을 말한다.
- Root(루트노드) : 트리에서 최상위 노드를 말한다.
- Leaf(리프노드) : 트리에서 최하위 노드를 말한다.
- Internal(가지노드) : 트리에서 최하위 노드를 제외한 모든 노드를 말한다.
- Level : 노드로 이루어진 각 층
- Height : 트리에서 Level의 수
### 이진트리
Binary Tree는 Root노드를 포함, Leaf노드를 제외한 __모든 노드의 자식이 두 개인 것__ 을 말한다. 공집합 역시 노드로 인정한다.
- 모든 Level이 가득 찬 이진트리인 Full Binary Tree(포화 이진 트리)
- 위에서 아래로, 왼족에서 오른쪽으로 순서대로 채워진 트리인 Complete Binary Tree(완전 이진 트리)가 있다.
- 높이가 H인 포화 이진 트리의 높이는 (2^H-1)개이다.
- 노드가 N개인 포화 이진트리의 높이는 log2(H+1)이다.

트리의 구현
1. 연결리스트 형태의 자료구조
```
class Node:
    Object data
    Node left_child, right_child
```

2. 일차원 배열을 이용한 구현
 - 배열로 포화 이진트리나 완전 이진트리를 구현했을 때, 노드의 개수 n에 대해서 i번째 노드에 parent(i) = i/2, left_child=2i, right_child = 2i+1의 인덱스 값을 갖는다.

### 트리순회
트리순회는 DFS 또는 BFS로 탐색하는데, 특히 이진 트리에서는 방문순서의 따라 크게 3가지 방식으로 나뉨.

 1. 전위(Pre-Order) 순회 (NLR)
 2. 중위(In-Order) 순회 (LNR)
 3. 후위(Post-Order) 순회 (LRN)

문자 L, R, N중 L은 현재 노드의 왼쪽 서브트리, R은 현재 노드의 오른쪽 서브트리, N은 현재 노드 자신을 의미한다.

### 힙 (Heap), 우선순위 큐 (Priority Queue)

- 완전 이진 트리의 일종으로, 부모의 값이 항상 자식보다 크거나 작아야 하는 힙 조건을 만족한다.
- 루트는 최댓값이거나, 최솟값임이 보장됨.
- 힙의 삽입, 삭제의 수행시간은 O(log2(N))이다.
- 최댓값 / 최솟값을 O(1)만에 찾을 수 있는 자료구조

__힙의 삽입__ 
>1. 트리의 가장 마지막 위치에 노드를 삽입한다.
>2. 추가된 노드와 그 부모 노드가 힙 조건을 만족하는지 확인한다.
>3. 만족하지 않는다면 부모와 자식의 키 값을 바꾼다.
>4. 조건에 만족하거나 추가된 노드가 루트에 도달할 때 까지 2~3을 반복한다.

__힙의 삭제__
>1. 루트노드를 삭제한다.
>2. 트리의 가장 마지막 노드를 루트 자리로 삽입한다.
>3. 바꾼 위치의 노드가 힙 조건을 만족하는지 확인한다.
>4. 만족하지 않는다면 왼쪽 자식과 오른쪽 자식중 적합한 노드와 키 값을 바꾼다.
>5. 조건을 만족하거나 리프 노드에 도달할 때까지 3~4를 반복한다.

__더 알아보기__
> 인덱스 트리(Indexed Tree), 트라이 (Trie)

 
## 그래프 (Graph)
---
정점과 간선의 집합이며, 일종의 Tree이다.
Undirected와 Directed Graph가 있는데, 방향성 유무로 결정된다.

Degree란 Undirected Graph에서 정점에 연결된 간선의 개수이다. Directed Graph에서의 Degree는 방향성이 있기 때문에 둘로 나뉘는데, 나가는 간선의 개수는 Outdegree, 들어오는 간선의 개수를 Indegree라 한다.

가중치 그래프란 간선에 가중치를 둔 그래프, 부분 그래프 란 한 그래프의 일부 정점 및 간선으로 이루어진 그래프.

그래프의 구현 방법 :

1. 인접 행렬 : 정방 행렬을 사용하여 구현. 연결 관계를 O(1)로 파악 가능. 공간복잡도는 O(2V)
2. 인접 리스트 : 리스트를 사용하여 구현. 정점간 연결 여부 파악에 오래 걸림. 공간복잡도는 O(E + V)
탐색 방법에는 깊이 우선 탐색(DFS, Depth First Search)와 너비 우선 탐색(BFS, Breadth First Search)이 있다.

깊이 우선 탐색은 깊숙히 들어가서 탐색하고 나오는 것이며 Stack을 통해 구현한다.
너비 우선 탐색은 임의이 한 정점에 대해 인접한 정점을 queue에 넣고, dequeue연산에서 나온 하나의 점점으로 드러아것 그 정점의 인접한 정점을 다시 Queue에 넣어서 탐색하는 방식이다. BFS로 찾은 경로는 최단 경로이다.

## 해싱(Hashing)
---
- 입력된 데이터(Key)를 해시 함수(Hashing Function)를 통해 얻은 주소로부터 그 위치를 직접 참조하는 방법이다.
- 탐색, 삽입, 삭제 연산 모두 해시 함수를 거치는 시간만 소요되기 때문에 일반적으로 O(1)의 시간복잡도를 가진다.
- Hash Table
    * 버킷(Bucket)과 슬롯(Slot)으로 구성된 이차원 배열
    - 버킷 개수 : 해시 함수를 통해 나오는 주소 값의 범위
    - 슬롯 개수 : 각 버킷에 저장할 수 있는 데이터(Key)의 개수
## 셋(Set)
---
* 셋(Set)
    - 집합을 정의하는 자료구조로 동일한 자료형을 모아놓은 것.
    - 집합의 모든 원소(Key)는 유일하다. 즉 중복이 허용되지 않는다.
    - 삽입, 삭제, 탐색의 세 가지 연산을 지원한다.
    - 구현 방식에 따라 해쉬 셋(Hash Set), 트리 셋(Tree Set)등이 존재한다.
* 해시 셋(Hash Set)
    - 해싱을 이용하여 데이터를 저장하는 방법.
    - 모든 연산이 O(1)에 수행되기 때문에 가장 빠르다
    - Key값을 나열했을 때 순서를 예측할 수 없다.
* 트리 셋(Tree Set)
    - 일반적으로 균형 이진 검색 트리 중 레드 블랙 트리로 구현되어 있다.
    - 모든 연산이 O(logN)에 수행된다.
    - Key 값을 나열 했을 때 정렬된 순서로 불러온다. 정렬 방식을 지정할 수 있다.
## 맵(Map)
---
- Key와 Value로 이루어진 객체를 저장하는 자료구조
- Set과 같이 Key값의 중복을 허용하지 않으며, value값은 제약이 없다.
- 삽입, 삭제, 탐색의 3가지 연산을 지원한다.
- 해시 테이블 내부의 값이 많아지면 해시 충돌 현상이 발생해 기본 연산의 시간이 길어진다.
- 구현방식에 따라 해쉬 맵(Hash Map), 트리 맵(Tree Map)등이 존재한다.

