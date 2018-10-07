#include "nodeAverage.h"
#include <maya/MFnPlugin.h>

MStatus initializePlugin(MObject obj)
{
	MStatus status;

	MFnPlugin fnPlugin(obj, "RomanVolodin", "1.0", "Any");

	status = fnPlugin.registerNode("myAverage", myAverageNode::id,  myAverageNode::creator, myAverageNode::initialize);

	CHECK_MSTATUS_AND_RETURN_IT(status);

	return MS::kSuccess;
}

MStatus uninitializePlugin(MObject obj)
{
	MStatus status;

	MFnPlugin fnPlugin(obj);

	status = fnPlugin.deregisterNode(myAverageNode::id);
	CHECK_MSTATUS_AND_RETURN_IT(status);

	return MS::kSuccess;

}