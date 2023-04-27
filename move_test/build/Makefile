# 'make'        build executable file
# 'make clean'  removes all .o and executable files
#
PLATFORM = linux
LIBS := -lm -pthread -ldl
ifeq ($(OS),Windows_NT)
	PLATFORM = windows
	LIBS = -lws2_32
endif

CC = gcc

CFLAGS = -Wall -g

# define any directories containing header files other than /usr/include
#

#includes
INCLUDES = -I../inc/$(PLATFORM)

#external libs
LFLAGS = -L../lib/$(PLATFORM)
# LIBS += -lftd2xx

# define the C source files
SRCS_DIR=../src

# John.shan
SRCS = $(SRCS_DIR)/c_test.c

OBJS_DIR=./$(PLATFORM)

# John.shan
OBJS = $(OBJS_DIR)/c_test.o 

# define the executable file 
# John.shan
SLIB = $(OBJS_DIR)/c_test.so


#
# The following part of the makefile is generic; it can be used to 
# build any executable just by changing the definitions above and by
# deleting dependencies appended to the file from 'make depend'
#

.PHONY: depend clean

# all:$(PROG)
all:$(SLIB)
	@echo  Compiled binary: $(SLIB)

# $(PROG):$(OBJS) 
# 	$(CC) $(CFLAGS) $(INCLUDES) -o $(PROG) $(OBJS) $(LFLAGS) $(LIBS)

$(SLIB):$(OBJS) 
	$(CC) $(CFLAGS) $(INCLUDES) -shared -o $(SLIB) $(OBJS) $(LFLAGS) $(LIBS)

# .c.o:
# 	$(CC) $(CFLAGS) $(INCLUDES) -c $<  -o $@  $(LFLAGS) $(LIBS)

$(OBJS_DIR)/%.o: $(SRCS_DIR)/%.c
	@mkdir -p $(dir $@)
	$(CC) $(CFLAGS) $(INCLUDES) -c -fPIC $<  -o $@  $(LFLAGS) $(LIBS)

clean:
	rm -rf ./$(PLATFORM)
	rm -rf $(PLATFORM)

depend: $(SRCS)
	makedepend $(INCLUDES) $^

# DO NOT DELETE THIS LINE -- make depend needs it