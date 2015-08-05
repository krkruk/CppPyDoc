void Coordinate::setDirection(char dirn)
{
    /*
     * Set direction of the coordinate according to the standards.
     * Input:
     * N, E - positive values
     * S, W - negative values
     * The function should be called once after setCoordinate()
     */
    this->dirn = dirn;
    setDirnValue();
}

void NMEA_VTG::setSpeedKmH(char *KmH)
{
    /*
     * Set Speed in Km/h in float variable
     * based on string input
     */
    char *p = strchr(KmH, '.');
    if(p == NULL)   //no coordinate found
        return;
    int found = p-KmH;   //find first occurence of '.'
    KmH[found] = ',';    //platform dependent
    this->speedKmH = strtod(KmH, NULL);
}
void TractionDriver::onJoyChanged(const Joystick &newState)
{
    /*------------------------------------------------------
     * This function reads data from joystick
     * everytime there is update of it.
     *
     * First it checks if joy is still connected
     * (to prevent reading from ampty list).
     * If joystick is connected, position of
     * proper axes are readed.
     * Then dead zone of joy (lower limit)
     * and max power is calculated.
     * Next step is to calculete averege and send
     * it to rover.
     *------------------------------------------------------*/
    if(newState.getIsConnected()){
        qint8 xAxis=0;
        qint8 yAxis=0;
        xAxis = static_cast<qint8>(newState.getAxisValue(Constants::TRACTION_X_AXIS));
        yAxis = static_cast<qint8>(newState.getAxisValue(Constants::TRACTION_Y_AXIS));
        qDebug()<<xAxis;
        xAxis = calculateLowerLimit(xAxis);
        yAxis = calculateLowerLimit(yAxis);
        xAxis = upperLimit->generate(xAxis);
        yAxis = upperLimit->generate(yAxis);
        xAxis = driveModeX->generate(xAxis);
        yAxis = driveModeY->generate(yAxis);

        qDebug()<< xAxis <<"   after";

        TractionMsg msg(tractionAddress,tractionPort,xAxis,yAxis);
        Network &network = Network::getInstance();
        network.send(msg);
    }
}

void CLASS::func1(char *str, bool isConnected = false) {
     //doc line 1,
     //doc line 2,
     //doc line 3
     return;
     //doc line extra1,
     //doc line extra2,
     //doc line extra3
}
