#pragma once
#include "Day.h"
#include <iostream>
#include <vector>

class Day2: public Day
{
public:
	Day2() = default;
	~Day2() = default;
	
	void Start() override;
	bool Test() override;
private:
	std::vector<std::string> GetInputVectorsCommaSeparated(std::string fileName) const;
	int ParseData(std::vector<int>& Data, int parameter1, int parameter2);
};
