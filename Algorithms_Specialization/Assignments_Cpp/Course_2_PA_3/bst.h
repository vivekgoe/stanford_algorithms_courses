#include <memory>
#include <algorithm>
#include <iostream>

using namespace std;

template <typename T>
class Node
{
public:
    T key, value;
    int height = 1;   // record height of node in tree
    int elements = 1; // record size of subtree starting at this node
    shared_ptr<Node> left = nullptr;
    shared_ptr<Node> right = nullptr;
    Node() {};
    Node(const T &k, const T &v) : key(k), value(v) {};
};

template <typename T>
class Bst
{
    shared_ptr<Node<T>> root = nullptr;
    shared_ptr<Node<T>> insert_recursive(const T &key, const T &value, shared_ptr<Node<T>> ptr);
    int get_elements(shared_ptr<Node<T>> ptr);
    int get_height(shared_ptr<Node<T>> ptr);
    int get_balance(shared_ptr<Node<T>> ptr);
    shared_ptr<Node<T>> left_rotate(shared_ptr<Node<T>> ptr);
    shared_ptr<Node<T>> right_rotate(shared_ptr<Node<T>> ptr);

public:
    shared_ptr<Node<T>> get_tree_root();
    int get_tree_height();
    int get_tree_elements();
    T select(const int &rank, shared_ptr<Node<T>> node);
    shared_ptr<Node<T>> search(const T &key);
    void insert(const T &key, const T &value);
    void inorder_traversal(std::ostream &os, shared_ptr<Node<T>> ptr)
    {
        if (ptr == nullptr)
        {
            return;
        }
        inorder_traversal(os, ptr->left);
        os << (*ptr).key << ": " << (*ptr).height << "," << (*ptr).elements << ", ";
        inorder_traversal(os, ptr->right);
    }
    void preorder_traversal(std::ostream &os, shared_ptr<Node<T>> ptr)
    {
        if (ptr == nullptr)
        {
            return;
        }
        os << (*ptr).key << ": " << (*ptr).height << "," << (*ptr).elements << ", ";
        preorder_traversal(os, ptr->left);
        preorder_traversal(os, ptr->right);
    }
    friend std::ostream &operator<<(std::ostream &os, Bst<T> bst)
    {
        bst.preorder_traversal(os, bst.root);
        os << "\n";
        return os;
    };
};

template <typename T>
shared_ptr<Node<T>> Bst<T>::get_tree_root()
{
    return root;
}

template <typename T>
T Bst<T>::select(const int &rank, shared_ptr<Node<T>> node)
{
    auto j = 0;
    if (node->left != nullptr)
    {
        j = node->left->elements;
    }
    if (rank == j + 1)
    {
        return node->key;
    }
    else if (rank < j + 1)
    {
        return select(rank, node->left);
    }
    else
    {
        return select(rank - j - 1, node->right);
    }
}

template <typename T>
int Bst<T>::get_tree_height()
{
    return get_height(root);
}

template <typename T>
int Bst<T>::get_tree_elements()
{
    return get_elements(root);
}

template <typename T>
shared_ptr<Node<T>> Bst<T>::search(const T &key)
{
    auto ptr = root;
    while (ptr != nullptr)
    {
        if (ptr->key == key)
        {
            return ptr;
        }
        else if (key < ptr->key)
        {
            ptr = ptr->left;
        }
        else
        {
            ptr = ptr->right;
        }
    }
    return nullptr;
}

template <typename T>
void Bst<T>::insert(const T &key, const T &value)
{
    if (root == nullptr)
    {
        root = make_shared<Node<T>>(key, value);
        return;
    }
    auto ptr = insert_recursive(key, value, root);
}

template <typename T>
shared_ptr<Node<T>> Bst<T>::insert_recursive(const T &key, const T &value, shared_ptr<Node<T>> ptr)
{
    if (ptr == nullptr)
    {
        ptr = make_shared<Node<T>>(key, value);
        return ptr;
    }

    if (key < ptr->key)
    {
        ptr->left = insert_recursive(key, value, ptr->left);
    }
    else
    {
        ptr->right = insert_recursive(key, value, ptr->right);
    }

    ptr->height = 1 + max(get_height(ptr->left), get_height(ptr->right));
    ptr->elements = 1 + get_elements(ptr->left) + get_elements(ptr->right);

    if (get_balance(ptr) < -1 && key > ptr->right->key)
    { // 2 back to back additions to right causing imbalance (Right-Right case)
        return left_rotate(ptr);
    }
    if (get_balance(ptr) < -1 && key < ptr->right->key)
    {                                          // addition to right followed by addition to left causing imbalance (Right-Left case)
        ptr->right = right_rotate(ptr->right); // rotate to right, this does not correct imbalance yet
        return left_rotate(ptr);               // rotating now is equivalent to previous case above
    }
    if (get_balance(ptr) > 1 && key < ptr->left->key)
    { // 2 back to back additions to left causing imbalance (Left-Left case)
        return right_rotate(ptr);
    }
    if (get_balance(ptr) > 1 && key > ptr->left->key)
    {                                       // addition to left followed by addition to right causing imbalance (Left-Right case)
        ptr->left = left_rotate(ptr->left); // rotate to left, this does not correct imbalance yet
        return right_rotate(ptr);           // rotating now is equivalent to previous case above
    }

    return ptr;
}

template <typename T>
shared_ptr<Node<T>> Bst<T>::left_rotate(shared_ptr<Node<T>> x)
{
    auto y = x->right;
    auto t = y->left;
    y->left = x;
    x->right = t;
    x->height = 1 + max(get_height(x->left), get_height(x->right));
    y->height = 1 + max(get_height(y->left), get_height(y->right));
    x->elements = 1 + get_elements(x->left) + get_elements(x->right);
    y->elements = 1 + get_elements(y->left) + get_elements(y->right);
    if (x == root)
    {
        root = y;
    }
    return y;
}

template <typename T>
shared_ptr<Node<T>> Bst<T>::right_rotate(shared_ptr<Node<T>> x)
{
    auto y = x->left;
    auto t = y->right;
    y->right = x;
    x->left = t;
    x->height = 1 + max(get_height(x->left), get_height(x->right));
    y->height = 1 + max(get_height(y->left), get_height(y->right));
    x->elements = 1 + get_elements(x->left) + get_elements(x->right);
    y->elements = 1 + get_elements(y->left) + get_elements(y->right);
    if (x == root)
    {
        root = y;
    }
    return y;
}

template <typename T>
int Bst<T>::get_elements(shared_ptr<Node<T>> ptr)
{
    if (ptr == nullptr)
        return 0;
    return ptr->elements;
}

template <typename T>
int Bst<T>::get_height(shared_ptr<Node<T>> ptr)
{
    if (ptr == nullptr)
        return 0;
    return ptr->height;
}

template <typename T>
int Bst<T>::get_balance(shared_ptr<Node<T>> ptr)
{
    if (ptr == nullptr)
        return 0;
    return get_height(ptr->left) - get_height(ptr->right);
}