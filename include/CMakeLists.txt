
set(${PROJECT_NAME}_public_headers
  "${CMAKE_CURRENT_LIST_DIR}/${PROJECT_NAME}/conancudalib.h"
)

target_sources(${PROJECT_NAME}
  PRIVATE
    ${${PROJECT_NAME}_public_headers}
)

set_target_properties(${PROJECT_NAME} PROPERTIES PUBLIC_HEADER "${${PROJECT_NAME}_public_headers}")

