cmake_minimum_required(VERSION 3.5)

project(task3)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# =====================================
# Service Generation
# =====================================

rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/PrimeFactors.srv"
)

# =====================================
# Launch Files
# =====================================

install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

# =====================================
# Python Scripts
# =====================================

install(
  PROGRAMS

  scripts/Task3A.py
  scripts/BonusTask3A.py
  scripts/Task3B.py
  scripts/Task3C.py
  scripts/Task3D_server.py
  scripts/Task3D_client.py

  DESTINATION lib/${PROJECT_NAME}
)

ament_package()