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

QString func4a(const QString& str) const
{
	//Return the string
	return str;
}

QString func4b(const QString& str) const{
	//Return the string
	return str;
}

QString func4c(const QString& str) const {
	//Return the string
	return str;
}

QString func4d(const QString& str) const
{
	/*
	 * Return the string
	 */
	return str;
}

QString func4e(const QString& str) const{
	/*
	 *Return the string
	 */
	return str;
}

QString func4f(const QString& str) const {
	/*
	 *Return the string
	 */
	return str;
}

std::vector &foo1a()
{
	//Return a vector1a
	return m_vec;
}
std::vector &foo1b(){
	/*
	 * Return a vector1b
	 */
	return m_vec;
}
std::vector &foo1c() {
	/*
	 * Return a vector1c
	 */
	return m_vec;
}

void TheClass::hello1a()
{
	/*
	 * This function says hello
	 */
	std::cout<<"Hello :D!";
}
void TheClass::hello1b(){
	/*
	 * This function says hello
	 */
	std::cout<<"Hello :D!";
}
void TheClass::hello1c()	{
	/*
	 * This function says hello
	 */
	std::cout<<"Hello :D!";
}
void TheClass::hello1d()
{
	//This function says hello
	std::cout<<"Hello :D!";
}
void TheClass::hello1e() {
	//This function says hello
	std::cout<<"Hello :D!";
}
void TheClass::hello1f()	{
	//This function says hello
	std::cout<<"Hello :D!";
}

void TheInline::helloInLine1a(){ /*Hello inline*/ std::cout<<"hello"; }
void TheInline::helloInLine1b() { /*Hello inline*/ std::cout<<"hello"; }
void TheInline::helloInLine1c() { /*Hello inline*/ 
std::cout<<"hello"; }
void TheInline::helloInLine1d() { /*Hello inline*/ 
	std::cout<<"hello"; 
}
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
