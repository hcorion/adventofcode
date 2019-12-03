#include "pch.h"
#include "Day2.h"
#include <vector>
#include <string>
#include <fstream>
#include <array>
#include <cassert>

void Day2::Start()
{
	auto Result = GetInputVectorsCommaSeparated("../AdventOfCode2019/Day2/input.txt");
	std::vector<int> data;
	for (std::string value : Result)
	{
		data.push_back(std::stoi(value));
	}

	{
		// Duplicate data because ParseData changes data
		auto newData = data;
		int FinalOutput = ParseData(newData, 12, 2);
		std::cout << "\nFinal Result: " << FinalOutput;
	}

	std::cout<< "2nd Part: \n";

	bool combinationFound = false;
	const int desiredEquation = 19690720;
	for(int x = 0; x <= 99; x++)
	{
		for(int y = 0; y <= 99; y++)
		{
			auto newData = data;
			int FinalOutput = ParseData(newData, x, y);
			if (FinalOutput == desiredEquation)
			{
				std::cout << "Parameters for " << desiredEquation << " are: " << x << " and " << y;
				combinationFound = true;
				break;
			}
		}
		if (combinationFound)
			break;
	}
}

std::vector<std::string> Day2::GetInputVectorsCommaSeparated(std::string fileName) const
{
	std::vector<std::string> result = std::vector<std::string>();
	std::ifstream inputFile;
	inputFile.open (fileName);
	if (inputFile.is_open())
	{
		std::string temp;
		char readChar;
		while ( inputFile.get(readChar) )
		{
			if (readChar == ',')
			{
				result.push_back(temp);
				temp = "";
				continue;
			}
			temp += readChar;
		}
		// Gotta add the character after the last comma
		result.push_back(temp);
		
		inputFile.close();
	}
	return result;
}

int Day2::ParseData(std::vector<int>& Data, int parameter1, int parameter2)
{
	// Input the program parameters
	Data[1] = parameter1;
	Data[2] = parameter2;
	
	int ExecutionIndex = 0;
	bool StopExecution = false;
	while (StopExecution == false)
	{
		switch (Data[ExecutionIndex])
		{
			// Addition opcode
		case 1:
			{
				Data[Data[ExecutionIndex+3]] = Data[Data[ExecutionIndex+1]] + Data[Data[ExecutionIndex+2]];
				break;
			}
			// Multiplication opcode
		case 2:
			{
				Data[Data[ExecutionIndex+3]] = Data[Data[ExecutionIndex+1]] * Data[Data[ExecutionIndex+2]];
				break;
			}
			// stop execution opcode
		case 99:
			{
				StopExecution = true;
				break;
			}
		}
		ExecutionIndex += 4;
	}
	return Data[0];
}

// Testing Framework

bool Day2::Test()
{
	// Part 1
	struct TestValues
	{
		std::vector<int> input;
		std::vector<int> expectedOutputVector;
		int expectedOutput;
		TestValues(std::vector<int> in, std::vector<int> outVec, int out)
		{
			input = in;
			expectedOutputVector = outVec;
			expectedOutput = out;
		}
	};

	std::array<TestValues, 4> values = {
		TestValues(std::vector<int>{1, 0, 0, 0, 99}, std::vector<int>{2, 0, 0, 0, 99}, 2),
		TestValues(std::vector<int>{2, 3, 0, 3, 99}, std::vector<int>{2, 3, 0, 6, 99}, 2),
		TestValues(std::vector<int>{2, 4, 4, 5, 99, 0}, std::vector<int>{2, 4, 4, 5, 99, 9801}, 2),
		TestValues(std::vector<int>{1, 1, 1, 4, 99, 5, 6, 0, 99}, std::vector<int>{30, 1, 1, 4, 2, 5, 6, 0, 99}, 30),
	};

	for (auto value : values)
	{
		int result = ParseData(value.input, value.input[1], value.input[2]);
		assert(result == value.expectedOutput);
		assert(value.input == value.expectedOutputVector);
	}
	return true;
}