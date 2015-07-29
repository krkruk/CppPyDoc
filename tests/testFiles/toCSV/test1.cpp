void func1a()
{
	/*Comment1a*/
	return;
}

void func2a()
{
	//Comment2a
	return;
}

void func1b(){
	/*Comment1b*/
	std::cout<<"Hello!";
	return;
}

void func2b(){
	//Comment2b
	std::cout<<"Hello!";
	return;
}


int func3a(float a, double b = 1.0f, bool c=false)
{
	/*
	 * Doc string func3a
	 * line2
	 */
	if( b != 0 )
		return a / b;
	else
		return 0;
}

int func3b(float a, double b = 1.0f, bool c=false){
	/*
	 * Doc string func3b
	 * line2
	 */
	if( b != 0 )
		return a / b;
	else
		return 0;
}


