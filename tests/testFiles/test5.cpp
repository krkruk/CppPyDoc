void TheClass::foo(int b,
		QString &name,
		QString defaultName = QString(""),
		bool isTrue=false) {
	/*
	* wierd function
	* example
	*/
	if( defaultName = "Hello")
	{
		name = "Hi there";
	}
	while b:
		b--;
	cout<<"Hehe"; //comment
}

void TheNS::TheClass::TheFooClass::fooNoComment(const QString &txt,
					std::vector<int> i,
					const std::vector<int> &input,
					float z = 15.02f) noexcept {
	for(auto elem : input){
		cout << elem;
	}
	//No comment to that class
}
void TheNS::TheClass::TheFooClass::fooX(const QString &txt,
					std::vector<int> i,
					const std::vector<int> &input,
					float z = 15.02f) 
noexcept 
{
	for(auto elem : input){
		cout << elem;
	}
	//No comment to that class
}

int TheNS::TheClass::TheFooClass::fooConst(const QString &txt,
					std::vector<int> i,
					const std::vector<int> &input,
					float z = 15.02f) const
noexcept {
	for(auto elem : input){
		cout << elem;
	}
	//No comment to that class
	return i;
}
