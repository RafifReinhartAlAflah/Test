#include <iostream>
#define LOG(x) std::cout << x << std::endl

class Robot {
    static int count_;
private:
    float x,y, ord;
    float noise;
public:
    Robot(): x(0), y(0), ord(0){count_++;}

    Robot(float xin, float yin, float ordin):x(xin), y(yin), ord(ordin){count_++;}

    ~Robot(){count_--;}

    int get_count(){
        return (int)count_;
    }
    void move_up(float val){
        this-> y += val;
        //+ noise
    }
    void move_down(float val){
        this-> y -= val;
        //+ noise
    }
    void move_left(float val){
        this-> x -= val;
        //+ noise
    }
    void move_right(float val){
        this-> x += val;
        //+ noise
    }
    float get_x(){
        return x;
    }

    void set_x(float xin){
        this-> x= xin;
    }

    float get_y(){
        return y;
    }

    void set_y(float yin){
        this -> y = yin;
    }

    float get_ord(){
        return ord;
    }

    void set_ord(float ordin){
        this -> ord = ordin;
    }

    void getdetails(){}
};

int Robot :: count_ = 0;
int main(){
    Robot r1(3.0,5.0,4.6);
    r1.set_ord(90);
    LOG(r1.get_count());
}