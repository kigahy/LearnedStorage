#include <iostream>
#include <locale>
#include <codecvt>
#include "libs/bridge.h"

std::string utf8_encode(const std::wstring& wstr);

int main() {
	std::wstring nickname = L"통신테스트";
	std::string game_data = init(nickname);

	while (!game_data.empty()) {
		std::string output = "C";
		game_data = submit(output);
		break;
	}

	close();
	return 0;
}
