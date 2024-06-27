#include <iostream>
using namespace std;

#define LOG(x) std::cout << x << std:endl

class Robot {
    static int count_;
private:
    float x,y,ord;
    float noise;
    static size_t count_;

public:
    Robot() : x(0), y(0), ord(0){count_++};

    Robot(float xin, float yin, float ordin) : x(xin), y(yin), ord(ordin){count_++}; 

    ~Robot() {count_--;};

    static int getCount() {
        return (int)count_;
    }

    float get_x(){ // Melakukan print posisi X robot
    return x;
    }

    void set_x(float xin){  // Setter untuk posisi robot X 
        this-> x= xin;
    }

    float get_y(){ // Melakukan print posisi Y dari robot
        return y;
    }

    void set_y(float yin){  // Setter untuk posisi robot Y
        this -> y = yin;
    }

    float get_ord(){ // Getter untuk orientasi robot dan Melakukan print orientasi dari robot
        return ord;
    }

    void set_ord(float ordin){ // Setter untuk orientasi robot
        this -> ord = ordin;
    }

    void moveUp(float val) {
        this-> y += val;
        //+ noise
    }

    void moveDown(float val) {
        this-> y -= val;
        //+ noise
    }

    void moveRight(float val) {
        this-> x += val;
        //+ noise
    }

    void moveLeft(float val) {
        this-> x -= val;
        //+ noise
    }

    // Robot(float x, float y){
    //     void prinStatus(){
    //         std::cout << "X = " << x << std::endl;
    //         std::cout << "Y = " << y << std::endl;
    //         std::cout << "Speed = " << speed << std::endl;
    //     }
    // }
};

int Robot::count = 0;

int main() {
    Robot r1(0, 0, 0);
    r1.getPos();
    r1.moveUp();
    r1.getPos();
    cout << "Number of Robots: " << Robot::getCount() << endl;
    return 0;
    Robot r1(3.0,5.0,4.6);
    r1.set_ord(90);
    LOG(r1.get_count());
}
