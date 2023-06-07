public class gb_sem_3 {
<<<<<<< HEAD
    public static class sList{
        private Node Head;
        private class Node{
=======
    public static class sList {
        private Node Head;

        private class Node {
>>>>>>> 2d8d846aa22b1d5e3a166dce96a4c0fb78b488bc
            private int value;
            private Node next;
        }

<<<<<<< HEAD
        void push(int value){
=======
        void push(int value) {
>>>>>>> 2d8d846aa22b1d5e3a166dce96a4c0fb78b488bc
            Node node = new Node();
            node.value = value;
            node.next = Head;
            Head = node;
        }

<<<<<<< HEAD
        Integer pop(){
            if(Head != null) {
=======
        Integer pop() {
            if (Head != null) {
>>>>>>> 2d8d846aa22b1d5e3a166dce96a4c0fb78b488bc
                Integer value = Head.value;
                Head = Head.next;
                return value;
            }
            return null;
        }

<<<<<<< HEAD
        void print(){
            Node current = Head;
            while (current != null){
=======
        void print() {
            Node current = Head;
            while (current != null) {
>>>>>>> 2d8d846aa22b1d5e3a166dce96a4c0fb78b488bc
                System.out.println(current.value);
                current = current.next;
            }
        }

<<<<<<< HEAD
        void pushBack(int value){
=======
        void pushBack(int value) {
>>>>>>> 2d8d846aa22b1d5e3a166dce96a4c0fb78b488bc
            Node node = new Node();
            node.value = value;

            Node current = Head;
<<<<<<< HEAD
            if(current != null) {
=======
            if (current != null) {
>>>>>>> 2d8d846aa22b1d5e3a166dce96a4c0fb78b488bc
                while (current.next != null) {
                    current = current.next;
                }
                current.next = node;
<<<<<<< HEAD
            }else{
=======
            } else {
>>>>>>> 2d8d846aa22b1d5e3a166dce96a4c0fb78b488bc
                Head = node;
            }
        }

<<<<<<< HEAD
        Node find(int value){
            Node current = Head;
            while (current != null){
                if(current.value == value){
=======
        Node find(int value) {
            Node current = Head;
            while (current != null) {
                if (current.value == value) {
>>>>>>> 2d8d846aa22b1d5e3a166dce96a4c0fb78b488bc
                    return current;
                }
                current = current.next;
            }
            return null;
        }
    }

<<<<<<< HEAD
    public static class dList{
        private Node Head;
        private Node Tail;
        private class Node{
=======
    public static class dList {
        private Node Head;
        private Node Tail;

        private class Node {
>>>>>>> 2d8d846aa22b1d5e3a166dce96a4c0fb78b488bc
            private int value;
            private Node next;
            private Node prev;
        }

<<<<<<< HEAD
        void pushFront(int value){
            Node node = new Node();
            node.value = value;
            if(Head != null) {
                Head.prev = node;
                node.next = Head;
            }else{
=======
        void pushFront(int value) {
            Node node = new Node();
            node.value = value;
            if (Head != null) {
                Head.prev = node;
                node.next = Head;
            } else {
>>>>>>> 2d8d846aa22b1d5e3a166dce96a4c0fb78b488bc
                Tail = node;
            }

            Head = node;
        }

<<<<<<< HEAD
        Integer popFront(){
            if(Head != null) {
                Integer value = Head.value;
                if(Head.next != null) {
                    Head = Head.next;
                    Head.prev = null;
                }else{
=======
        Integer popFront() {
            if (Head != null) {
                Integer value = Head.value;
                if (Head.next != null) {
                    Head = Head.next;
                    Head.prev = null;
                } else {
>>>>>>> 2d8d846aa22b1d5e3a166dce96a4c0fb78b488bc
                    Head = null;
                    Tail = null;
                }
                return value;
            }
            return null;
        }

<<<<<<< HEAD
        void print(){
            Node current = Head;
            while (current != null){
=======
        void print() {
            Node current = Head;
            while (current != null) {
>>>>>>> 2d8d846aa22b1d5e3a166dce96a4c0fb78b488bc
                System.out.println(current.value);
                current = current.next;
            }
        }

<<<<<<< HEAD
        void pushBack(int value){
            Node node = new Node();
            node.value = value;

            if(Tail != null){
                Tail.next = node;
                node.prev = Tail;
            }else{
=======
        void pushBack(int value) {
            Node node = new Node();
            node.value = value;

            if (Tail != null) {
                Tail.next = node;
                node.prev = Tail;
            } else {
>>>>>>> 2d8d846aa22b1d5e3a166dce96a4c0fb78b488bc
                Head = node;
            }

            Tail = node;
        }

<<<<<<< HEAD
        Node find(int value){
            Node current = Head;
            while (current != null){
                if(current.value == value){
=======
        Node find(int value) {
            Node current = Head;
            while (current != null) {
                if (current.value == value) {
>>>>>>> 2d8d846aa22b1d5e3a166dce96a4c0fb78b488bc
                    return current;
                }
                current = current.next;
            }
            return null;
        }

<<<<<<< HEAD
        Node revFind(int value){
            Node current = Tail;
            while (current != null){
                if(current.value == value){
=======
        Node revFind(int value) {
            Node current = Tail;
            while (current != null) {
                if (current.value == value) {
>>>>>>> 2d8d846aa22b1d5e3a166dce96a4c0fb78b488bc
                    return current;
                }
                current = current.prev;
            }
            return null;
        }
    }
<<<<<<< HEAD
=======

>>>>>>> 2d8d846aa22b1d5e3a166dce96a4c0fb78b488bc
    public static void main(String[] args) {
        dList list = new dList();

        list.pushBack(1);
        list.pushBack(2);
        list.pushBack(3);

        list.print();

        System.out.println(list.popFront());

        list.print();

    }
}
