package com.example.main;
import com.example.libraries.Bridge;

public class Main {
	
	private static String NICKNAME = "통신테스트";
	
    public static void main(String[] args) {
        Bridge bridge = new Bridge();
        String gameData = bridge.init(NICKNAME);
        
        while (gameData.length() > 0) {
        	String output = "C";
        	gameData = bridge.submit(output);
        	break;
        }

        bridge.close();
    }
}
