#pragma once

#include "behaviortree_cpp/action_node.h"


// SyncActionNode that prints a message to the console
class Print : public BT::SyncActionNode
{
public:
  Print(const std::string& name, const BT::NodeConfig& config);

  static BT::PortsList providedPorts();

  virtual BT::NodeStatus tick() override;
};
