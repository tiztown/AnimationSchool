#include "nodeAverage.h"
#include <maya/MFloatVector.h>

MTypeId myAverageNode::id(0x00000232);

MObject myAverageNode::aInValueA; 
MObject myAverageNode::aInValueB;
MObject myAverageNode::aOutValue;


myAverageNode::myAverageNode()
{
}

myAverageNode::~myAverageNode()
{
}

void* myAverageNode::creator()
{
	return new myAverageNode();
}


MStatus myAverageNode::compute(const MPlug& plug, MDataBlock& data)
{
	MStatus status;

	if (plug != aOutValue)
	{
		return MS::kUnknownParameter;
	}

	MFloatVector inputA = data.inputValue(aInValueA, &status).asFloat3();
	MFloatVector inputB = data.inputValue(aInValueB, &status).asFloat3();

	MFloatVector output = data.outputValue(aOutValue, &status).asFloat3();

	output = (inputA + inputB)/2;

	MDataHandle hOutput = data.outputValue(aOutValue, &status);
	CHECK_MSTATUS_AND_RETURN_IT(status);

	hOutput.set3Float(output[0], output[1], output[2]);
	hOutput.setClean(); 
	data.setClean(plug);

	return MS::kSuccess;

}


MStatus myAverageNode::initialize()
{
	MStatus status;
	MFnNumericAttribute nAttr;

	aOutValue = nAttr.create("outValue", "outValue", MFnNumericData::k3Float);
	nAttr.setWritable(false);
	nAttr.setStorable(true);
	addAttribute(aOutValue);

	aInValueA = nAttr.create("inValueA", "inValueA", MFnNumericData::k3Float);
	nAttr.setKeyable(true);
	addAttribute(aInValueA);
	attributeAffects(aInValueA, aOutValue);

	aInValueB = nAttr.create("inValueB", "inValueB", MFnNumericData::k3Float);
	nAttr.setKeyable(true);
	addAttribute(aInValueB);
	attributeAffects(aInValueB, aOutValue);

	return MS::kSuccess;


}
