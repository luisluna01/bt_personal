#include "bt_practice/behaviors/print.hpp"


Print::Print(const std::string& name, const BT::NodeConfig& config)
: BT::SyncActionNode(name, config)
{}


BT::PortsList Print::providedPorts()
{
  return {
    BT::InputPort<std::string>("message")
  };
}


BT::NodeStatus Print::tick()
{
  // Check if port is valid
  BT::Expected<std::string> maybe_message = getInput<std::string> ("message");
  if(!maybe_message)
  {
    throw BT::RuntimeError("missing required input [message]: ", maybe_message.error());
  }

  // Print message
  std::string message = maybe_message.value();
  std::cout << "[" << this->name() << "]: " << message << std::endl;

  return BT::NodeStatus::SUCCESS;
}
