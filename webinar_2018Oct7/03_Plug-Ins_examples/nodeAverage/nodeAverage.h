#ifndef MYAVERAGENODE_H
#define MYAVERAGENODE_H

#include <maya/MPxNode.h>
#include <maya/MFnNumericAttribute.h>

#include <math.h>

class myAverageNode : public MPxNode
{
public:
	myAverageNode(); 
	virtual ~myAverageNode();
	static void* creator();

	virtual MStatus compute(const MPlug& plug, MDataBlock& data);

	static MStatus initialize();

	static MObject aInValueA;
	static MObject aInValueB;
	static MObject aOutValue;

	static MTypeId id;
};

#endif
