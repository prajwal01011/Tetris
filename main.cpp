#include<iostream>

using namespace std;

wstring tetromino[7];
int nFieldWeidth=12;
int nFieldHeight=18;
unsigned char *pFeild=nullptr;

int rotate(int px,int py,int r){
    
    switch(r%4){
        case 0:return py*4+px;          //case 0 deg rotate
        case 1:return 12+py-(px*4);     //case 90 deg rotate
        case 2:return 15-(py*4)-px;     //case 180 deg rotate
        case 4:return 3+(px*4)-py;      //case 270 deg rotate
    }
    return 0;
}

int main(){

    cout<<"hello tetris\n";

    //building assets
    
    tetromino[0].append(L"..X.");
    tetromino[0].append(L"..X.");
    tetromino[0].append(L"..X.");
    tetromino[0].append(L"..X.");

    tetromino[1].append(L"..X.");
    tetromino[1].append(L".XX.");
    tetromino[1].append(L".X..");
    tetromino[1].append(L"....");

    tetromino[2].append(L".X..");
    tetromino[2].append(L".XX.");
    tetromino[2].append(L"..X.");
    tetromino[2].append(L"....");

    tetromino[3].append(L"....");
    tetromino[3].append(L".XX.");
    tetromino[3].append(L".XX.");
    tetromino[3].append(L"....");

    tetromino[4].append(L"..X.");
    tetromino[4].append(L".XX.");
    tetromino[4].append(L"..X.");
    tetromino[4].append(L"....");

    tetromino[5].append(L"....");
    tetromino[5].append(L".XX.");
    tetromino[5].append(L"..X.");
    tetromino[5].append(L"..X.");

    tetromino[6].append(L"....");
    tetromino[6].append(L".XX.");
    tetromino[6].append(L".X..");
    tetromino[6].append(L".X..");




    
    return 0;
}