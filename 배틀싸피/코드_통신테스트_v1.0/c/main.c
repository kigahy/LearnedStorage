#include <stdio.h>
#include <wchar.h>
#include "libs/bridge.h"

int main() {
    wchar_t nickname[] = L"통신테스트";
    char* game_data = init(nickname);

    while (game_data != NULL) {
        char output[] = "C";
        game_data = submit(output);
		break;
    }

    close();
    return 0;
}
