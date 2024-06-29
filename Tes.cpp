#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

// '''String Operation'''
// int main()
// {
//print String
//cara 1.
//     // std::cout << "Hello, World! \n" ;
//     // std::cout << "Hahaha" << std::endl;
//     // std::cout << "LOL!" ;
// // <<std::endl; == \n , fungsinya sama" untuk membuat baris baru
  

//cara 2.
//     // vector<string> msg {"woi ! Rafif Reinhart Al Aflah"};

//     // for (const string & word : msg)
//     // {
//     //     cout << word << " ";
//     // }
//     // cout << endl;

//cara 3.
    // int main(){
    //     std::string greeting = "Halloo";
    //     std::string name = " Rapip";
    //     std::cout << greeting + name << std::endl;
    // }

 
// }

// '''String and Integer Operation'''
// int main()
// {
// //1.
//     // int age;
//     // std::cout << "Enter your age: ";
//     // std::cin >> age;
//     // std::cout << "Your age 2 years ago was: " << age - 2 << std::endl;
//     // return 0; //menunjukkan program berhasil dieksekusi

// //2.
//     // int n,xo;

//     // cout <<"n: ";
//     // cin >> n;
//     // cout << "xo:";
//     // cin >> xo;
//     // //mencari banyak kelipatan
//     // int pos = 0;
//     // int i = 0;
//     // for (i; pos < xo; i++)(
//     //     pos += n
//     // );
//     // cout << i;
// }

// '''Integer Operation'''
// int main(){
//     int num;

//     std::cout << "Enter a number: ";
//     std::cin >> num;

//     if (num > 0){
//         std::cout << "Positive number" << std::endl;
//     }

//     else if (num < 0){
//         std::cout << "Negative number" << std::endl;
//     }

//     else{
//         std::cout << "Zero" << std::endl;
//     }
// }

//'''desimal/ pecahan'''
int main(){
    // double nilai = 98.8;
    // double tinggi = 170.5;
    // std::cout << nilai <<"\n";
    // std::cout << "Tinggi kamu sekarang: "<<tinggi << "cm";

    // int correct = 8;
    // int questions = 10;
    // double score = (double)correct/questions *100;
    // //harus ubah tipe data int menjadi double agar bisa di bagi

    // std::cout << score << " %";

    // double correct = 8;
    // int questions = 10;
    // double score = correct/questions *100;
    // //harus ubah tipe datanya menjadi double agar bisa di bagi

    // std::cout << score << " %";

    //karena tipe int saat di bagi akan menghasilkan bil.bulat
    //maka dari itu harus diubah menjadi tipe double terlebih dahulu
}

//'''inisiasi yang sama dengan fungsi yang berbeda'''
// namespace first{
//     int x = 10;
// }

// namespace second{
//     int x = 5;
// }

// int main(){
//     using namespace second;

//     std::cout << first::x << "\n"; //dapat mengambil inisiasi x fungsi "first" 
//     //dengan menyantumkan nama fungsi tersebut di depan X
    
//     using std::cout; //mempersingkat sehingga tidak perlu menulis "std::" di awalan
//     cout << x; //karena telah menggunakan fungsi second
//     //maka dia akan menampilkan nilai x di fungsi second
// }

//'''Similarity between typedef and using untuk tipe data dalam mempersingkat code'''
//1.
// typedef std::string text_t; //harus diakhir "_t"
// typedef int number_t;
//2. using lebi enak
// using text_t = std::string;
// using number_t = int;

// int main(){
//     using std::cout;
//     text_t firstName = "Rafif"; //firstName bertipe string
//     number_t age = 18;

//     //bebas mau diinisiasi dlu di atas std::cout nya / tulis satu"
//     cout<< firstName << "\n";
//     std::cout << age;
// }

// '''Looping'''
// int main() {
// //1. While loop
//     int i = 1; //inisiasi
//     // The while loop continues as long as the condition (i <= 5) is true
//     while (i <= 5) {
//         std::cout << i << " ";  // " " agar membuat jarak spasi antar angka 
//         i++;
//     }
//     std::cout << std::endl;

// //2. For loop
//     for (int i = 1; i <= 5; i++) {
//     std::cout << i << " ";
//     }

//     std::cout << std::endl;
//     return 0;
// }

//'''Array'''
// int main() {
//     int numbers[5] = {1, 2, 3, 4, 5};

//     // Output the third element (index 2) of the array.
//     std::cout << "Third element: " << numbers[1] << std::endl;
//     return 0;
// }

//'''Function'''
// int add(int a, int b){
//     return a + b;
// }

// int main(){
//     std::cout << "Sum: " << add(3,4) << std::endl;
// }

//'''pointer'''
// int main(){
//     int num = 42;
//     int *ptr = &num; // '*' dan '&' untuk membaca memori
//     std::cout << "Value at pointer: " << *ptr << std::endl; //print menggunakan '*' untuk print nilai dan tanpa '*' untuk melihat tersimpan di memori mana
// }

//'''Structure'''
// struct Point{
//     int x; //koordinat x
//     int y; //koordinat y
// };

// int main(){
//     Point p; //inisiasi p sebagai Point

//     p.x = 3;
//     p.y = 5;

//     std::cout << "Point: (" << p.x << "," << p.y << ")" << std::endl;
// }

//'''Enums'''
// enum Day {SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY};
// // mirip dictionary kaya list cuma pake kurung kurawal
// int main(){
//     Day today = TUESDAY; //inisiasi today sebagai Day
//     std::cout << "Today is day " << today << std::endl;
// }

//'''File handling-Writing
// int main(){
//     std::ofstream file("example.txt"); //membuat file baru bernama example.txt

//     file << "Hello, Rapip!"; //di dalam example.txt berisi tulisan Hello, Rapip!
//     file.close(); //jangan lupa tutup file setelah menulis :)
// }

//'''File handling-Reading
// int main(){
//     std::ifstream file("example.txt"); //baca isi dalem file example.txt
//     std::string content; //awalan konten yang akan dibaca
//     for (int i = 0; i <= 2; i++){
//         getline(file, content); //baca isi dari file per baris
//         std::cout << "File Content: " << content << std::endl;
//     }
//     file.close();
// }

//'''Dynamic Memory Allocation'''

// int main(){
//     int *arr = new int[5];
//     for (int i = 0; i < 5; i++){
//         arr[i] = i + 1; //memasukkan index [0] dengan nilai 1 hingga index [4] dengan nilai 5
//     }
//     std::cout << "Dynamic Array: ";
//     for (int i = 0; i < 5; i++){
//         std::cout << arr[i] << " ";
//     }
    //di bawah ini kurang tahu apa gunanya
    // delete[] arr;
    // std::cout << std::endl;
// }

//'''Object-Oriented Programming'''
// Definition of the Rectangle class
// class Rectangle {
//     public: //inisiasi tipe data
//         int length;
//         int width;
//         int area() { // Fungis operasi untuk menghitung area segiempat 
//             return length * width;
//         }
// };
// // Main function
// int main() {
//     Rectangle rect; //inisiasi rect sebagai Rectangle
//     rect.length = 4;
//     rect.width = 3;
//     // Calculating and displaying the area of the rectangle
//     std::cout << "Rectangle Area: " << rect.area() << std::endl;
// }

//'''Operator overloading'''
// Definition of the Complex class
// class Complex {
//   public:
//     int real;
//     int imag;
//     // Operator overloading for addition
//     Complex operator+(const Complex &c) {
//         Complex temp;
//         temp.real = real + c.real;
//         temp.imag = imag + c.imag;
//         return temp;
//     }
// };

// // Main function
// int main() {
//     // Creating objects of the Complex class
//     Complex a, b, result;
//     // Assigning values to complex numbers
//     a.real = 3; a.imag = 2;
//     b.real = 1; b.imag = 7;
//     // Using the overloaded + operator to add complex numbers
//     result = a + b;
//     // Displaying the sum of complex numbers
//     std::cout << "Sum: " << result.real << " + " << result.imag << "i" << std::endl;
// }

//'''Inheritance'''
// Base class: Shape
// class Shape {
//     public:
//         // Member function in the base class
//         void display() {
//             std::cout << "Shape" << std::endl;
//         }
// };
// // Derived class: Circle, inherits from Shape
// class Circle : public Shape {
//     public:
//         // Overriding the display function in the derived class
//         void display() {
//             std::cout << "Lingkaran" << std::endl;
//         }
// };
// // Main function
// int main() {
//     // Creating an object of the derived class Circle
//     Circle circle;
//     // Calling the overridden display function in the Circle class
//     circle.display();
// }

//'''Polymorphism'''
// Base class: Animal
// class Animal {
//     public:
//         // Virtual function in the base class
//         virtual void sound() {
//             std::cout << "Animal Sound" << std::endl;
//         }
// };
// // Derived class: Dog, inherits from Animal
// class Dog : public Animal {
//     public:
//         // Overriding the virtual function in the derived class
//         void sound() override {
//             std::cout << "Woof!" << std::endl;
//         }
// };
// // Main function
// int main() {
//     // Creating a pointer to the base class (Animal) and assigning it the address of an object of the derived class (Dog)
//     Animal *ptr = new Dog();
//     // Calling the virtual function using the pointer, which resolves to the overridden function in the Dog class
//     ptr->sound();
//     // Deleting the dynamically allocated object
//     delete ptr;
//     return 0;
// }

//'''Templates'''
// template <typename T>
// T add(T a, T b) { //Fungsi T dengan parameter a dan b dapat digunakan oleh tipe integer maupun float
//     return a + b;
// }

// int main() {
//     std::cout << "Sum: " << add(3, 4) << std::endl;
//     std::cout << "Sum: " << add(2.5, 3.5) << std::endl;
//     return 0;
// }

//'''Standard Template Library - Vector
// int main() {
//     std::vector<float> numbers = {1, 2, 3};
//     numbers.push_back(6); //menambahkan angka 6 di akhir urutan Array numbers di atas
//     std::cout << "Vector Size: " << numbers.size() << std::endl; //sehingga Array yang awalnya berisi 3, lalu ditambahkan angka baru(6).
//     //akhirnya sekarang Array berisi 4 angka
//     return 0;
// }

