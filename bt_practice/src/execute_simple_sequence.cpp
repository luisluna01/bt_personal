#include "behaviortree_cpp/bt_factory.h"
#include "ament_index_cpp/get_package_share_directory.hpp"

// Print behavior
#include "bt_practice/behaviors/print.hpp"


// Tree executer for the SimpleSequenceExample behavior tree
int main()
{
  BT::BehaviorTreeFactory factory;

  // Register nodes
  factory.registerNodeType<Print>("Print");

  // Register behaivor tree
  std::string share_path = ament_index_cpp::get_package_share_directory("bt_practice");
  factory.registerBehaviorTreeFromFile(share_path + "/trees/simple_sequence_example.xml");

  // Create and run tree
  BT::Tree tree = factory.createTree("SimpleSequenceExample");

  // Tick tree once
  std::cout << "Sending one tick signal..." << std::endl;
  tree.tickOnce();
  std::cout << "Finished executing Behavior Tree..." << std::endl;

  return 0;
}
