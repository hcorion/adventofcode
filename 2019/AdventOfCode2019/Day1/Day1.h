#pragma once
#include "Day.h"
#include <vector>

class Day1 : public Day
{
public:
	Day1();
	~Day1();
	void Start() override;
	bool Test() override;
private:
	std::vector<std::string> GetInputVectors(std::string fileName) const;
	std::vector<int> CalculateFuelInput(const std::vector<int> moduleMasses);
	int CalculateFuelFromMass(int mass) const;
	int GetFinalSum(std::vector<int> moduleMasses);
	int GetSubFuel(int Fuel);
};
