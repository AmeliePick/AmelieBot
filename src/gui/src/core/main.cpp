#include "amelie.h"


int main(int argc, char *argv[])
{
    AmelieApplication* amelie = AmelieApplication::getInstance();
    return amelie->main(argc, argv);
}
