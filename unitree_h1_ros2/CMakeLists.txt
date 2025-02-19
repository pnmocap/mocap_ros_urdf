cmake_minimum_required(VERSION 3.10)
project(unitree_h1_ros2)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)

# Install directories
foreach(dir launch meshes urdf)
  install(DIRECTORY ${dir}/
          DESTINATION share/${PROJECT_NAME}/${dir})
endforeach(dir)

# Install README and LICENSE
install(FILES README.md
        DESTINATION share/${PROJECT_NAME})

install(FILES LICENSE
        DESTINATION share/${PROJECT_NAME})     

# Main ament package command
ament_package()
