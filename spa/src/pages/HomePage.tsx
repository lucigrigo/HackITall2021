import * as React from "react";
import { useNavigate } from "react-router-dom";
import "../csss/HomePage.css";
import logo from '../img/logo_softlink.png';

interface Props {
}

const HomePage: React.FC<Props> = () => {
    const navigate = useNavigate();
    const accessSearchJobs = () => {
        let path= '/search-jobs';
        navigate(path);
    }

    const accessSearchCandidates = () => {
        let path = '/search-candidates';
        navigate(path)
    }

    return (
        <div className="page">
            <div className="container cntr">
                <img className="logo" src={logo} alt="Logo" />
            </div>
            <div className="cntr mrgn1">
                <h1 className="qstn">
                    WHICH SIDE ARE YOU ON?
                </h1>
            </div>
            <div className="panel_container">
                <div className="select_panel">
                    <div className="box">
                        <div className="box_title">
                            <h1>I am a recruiter.</h1>
                            <h2>I want to find candidates.</h2>
                        </div>
                        <div className="box_descr">
                            <span>
                                Select job title, required skills, location and get your future employees.
                            </span>
                        </div>
                        <div className="box_button">
                            <button className="button_style" onClick={accessSearchCandidates}>Find candidates</button>
                        </div>
                    </div>
                    <div className="sep">
                        <div className="line_sep"></div>
                        <div className="or_sep">OR</div>
                        <div className="line_sep"></div>
                    </div>
                    <div className="box">
                        <div className="box_title">
                            <h1>I am candidate.</h1>
                            <h2>I want to find job opportunities.</h2>
                        </div>
                        <div className="box_descr">
                            <span>
                                Select job title, your skills, your location and get your possible employers.
                            </span>
                        </div>
                        <div className="box_button">
                            <button className="button_style" onClick={accessSearchJobs}>Find jobs</button>
                        </div>
                    </div>
                </div>
            </div>
            

        </div>
       
    );
}

export default HomePage;