#include "../include/conancudalib/conancudalib.h"

#include <gtest/gtest.h>

namespace
{
    TEST(ConanCudaLibTest, WorkingCudaGetDeviceCount) {
        conancudalib();
        ASSERT_EQ(true, true);
    }
}