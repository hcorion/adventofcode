#pragma once
class Day
{
public:
	Day() = default;
	~Day() = default;

	virtual void Start() = 0;

	/**
	 * \brief 
	 * \return Returns true if the test succeeded, false if not
	 */
	virtual bool Test() = 0;
};

