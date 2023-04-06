# Polymorphism

As a practical exercise, try to overload the addition operator yourself. The method `add()` is used to overload it. It is called when objects of a class that have this method appear in the addition operation, specifically on the left side. This means that the object **a** in the expression **a + b** must have the `add()` method. Object **b** can be anything, but it is often an object of the same class. Object **b** will be automatically passed to the `add()` method as the second argument (the first is **self**).

Note that in Python there is also a right-sided method for overloading addition - `radd()`.

According to the polymorphism principle of OOP, the `add()` method can return anything. It may not return anything at all and "silently" make changes to existing objects. For example, in your program, the addition overload method **will return a new object of the same class**.

---

Task 5 from course: <https://younglinux.info/oopython/course>
