import * as React from "react";

import "../csss/HomePage.css";
import logo from '../logo_softlink.png';
interface Props {
}

const HomePage: React.FC<Props> = () => {
    return (
        <div>
            <div className="container ctr">
                <img className="logo" src={logo} alt="Logo" />
            </div>

        </div>
       
    );
}

export default HomePage;