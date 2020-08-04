#include "logger.h"



Logger::Logger()
{
    this->fileWrite = std::ofstream("interpreter_log.txt");
}



Logger* Logger::create()
{
    static Logger* instance = new Logger();
    return instance;
}



void Logger::writeLog(char* data)
{
    this->fileWrite << data << '\n\n';
}
