#include <string>      // for std::string
#include <fstream>     // for std::ofstream
#include <ctime>       // for std::time, std::localtime, std::asctime
#include <cstring>     // for std::strlen
#include <cstdio>      // for printf

#include <stdio.h>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <omp.h>
#include <iostream>

#include <cstdint>

#include "tools.hpp"

namespace tools {
	static timespec  performanceCountStart;
	static timespec performanceCountStop;

	void start_time(void) 
	{
		clock_gettime(CLOCK_MONOTONIC, &performanceCountStart);
	}

	void stop_time(void) 
	{
		clock_gettime(CLOCK_MONOTONIC, &performanceCountStop);
	}

	void stop_time_and_calc_sec(float* delay) 
	{
	    stop_time();		
        *delay = static_cast<float>( (performanceCountStop.tv_sec - performanceCountStart.tv_sec) + (performanceCountStop.tv_nsec - performanceCountStart.tv_nsec) / 1e9  );
	}

    std::string formatWithCommas(double val)
    {
        std::stringstream ss;
        ss.imbue(std::locale("en_US.UTF-8"));   // add thousands separators
        ss << std::fixed << std::setprecision(2) << val;
        return ss.str();
    }
    
	std::string formatWithCommas(uint64_t value)
	{
		std::stringstream ss;
		ss.imbue(std::locale("en_US.UTF-8"));
		ss << std::fixed << value;
		return ss.str();
	}
	
	std::string formatPrefix(double val)
	{
		const std::string prefixes[5] = { "MEGA", "GIGA", "TERA", "PETA", "EXA" };
		const double prefix_multipliers[5] = { 1000000,1000000000,1000000000000,1000000000000000,1000000000000000000 };
		std::string prefix = "";
		for (int i = 4; i >= 0; i--)
		{
			if (val > prefix_multipliers[i])
			{
				val = (val / (double)prefix_multipliers[i]);
				prefix = prefixes[i];
			}
		}

		std::stringstream ss;
		ss.imbue(std::locale("en_US.UTF-8"));
		ss << std::fixed << val << " " << prefix;
		return ss.str();
	}
	
	void logMessage(std::string msg, std::string log_name)
    {
        std::ofstream out;
        out.open(log_name, std::ios::app);
        if (out.is_open())
        {
            std::time_t time_date = std::time(nullptr);
		    char* time_str = std::asctime(std::localtime(&time_date));

	      		// Remove the newline character added by std::asctime
		     time_str[std::strlen(time_str) - 1] = '\0';

		     out << time_str << " " << msg << std::endl;
        }
        else
	        printf("\n!!!ERROR open file %s!!!\n", log_name.c_str());
	        
        out.close();
    }
}
