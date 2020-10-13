#ifndef AMELIE_H
#define AMELIE_H

class Amelie
{
private:
    void* classInstance;

    Amelie() = delete;
    Amelie(const char* appLanguage);
    Amelie(const Amelie &) = delete;


    void doAction(const char* inputType);

    void updateProgramList();

public:
    static Amelie* getInstance(const char* appLanguage);

    void changeLanguage(const char* language);

    char* conversation(const char* userInput);

    void tts(const char* pharse);

    void update();

    const char* getPathToProgram(const char* programName);

    void addProgram(const char* program, const char* path);

    bool getVoice();

    void setVoice(bool value);

    const char* getUserInput();


    ~Amelie();
};

#endif // AMELIE_H
