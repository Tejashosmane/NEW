class Person{
    String Name="tejas";
    int age=20;
    public void Printname(){
        System.out.println(Name);
    }
}

class Employee extends Person{
    public void Printage(){
        System.out.println(age);
    }
}

public class solution{
    public static void main(String[] args) {
        Person p1=new Employee();
        p1.Printname();
    }
}