#ifndef MYTESTCMD_H
#define MYTESTCMD_H

#include <maya/MPxCommand.h> 
#include <maya/MGlobal.h>
#include <maya/MObject.h>
#include <maya/MSyntax.h>

class myTestCmd : public MPxCommand
{
public:
	myTestCmd();
	virtual MStatus doIt(const MArgList& argList); 
	static void* creator();
	 

};

#endif
