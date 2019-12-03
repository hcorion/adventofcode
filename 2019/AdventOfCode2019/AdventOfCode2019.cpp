// AdventOfCode2019.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <string>
#include "Day.h"
#include "Day1/Day1.h"
#include "Day2/Day2.h"

const int NumberOfAdventDays = 2;

// Used to auto-launch a specific day
const int InitialDebugValue = 2;

int main(int argc, char *argv[])
{
	int Input = 0;

	// If we just want to test one of the advents by default
	if (InitialDebugValue > 0)
		Input = InitialDebugValue;
	
	while (Input <= 0 || Input < NumberOfAdventDays)
	{
		std::cout << "Which Advent Of Code Day would you like to run?\n";
		std::cin >> Input;
		std::cin.clear();
		
		if (Input <= 0 || Input < NumberOfAdventDays)
		{
			std::cout << "The input " << Input << " is not valid. Please try again\n";
		}
	}
	Day* day = nullptr;
	switch (Input)
	{
	case 1:
		{
			Day1 newDay = Day1();
			day = &newDay;
			break;
		}
	case 2:
		{
			Day2 newDay = Day2();
			day = &newDay;
			break;
		}
			
	default:
		{
			std::cout << "That day is listed, but unfortunately is not actually implemented\n";
			break;
		}
	}
	if (day != nullptr)
	{
		if (day->Test())
		{
			std::cout << "All tests succeeded!\n";
		}
		else
		{
			std::cout << "Tests did not succeeded, stopping.\n";
			return 0;
		}
		day->Start();
	}
	
	return 0;
}