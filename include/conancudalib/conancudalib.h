#pragma once


#ifdef _WIN32
  #define CONANCUDALIB_EXPORT __declspec(dllexport)
#else
  #define CONANCUDALIB_EXPORT
#endif

CONANCUDALIB_EXPORT void conancudalib();
