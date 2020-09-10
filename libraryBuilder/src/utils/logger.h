#pragma once
#include <fstream>

class Logger
{
private:
    Logger();
    Logger(const Logger &);



    std::ofstream fileWrite;

public:
    static Logger* create();


    void writeLog(const char* data);
};