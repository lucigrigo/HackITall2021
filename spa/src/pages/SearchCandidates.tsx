import * as React from "react";
import { TagsInput } from "react-tag-input-component";
import { useNavigate } from "react-router-dom";
import FancyTable from "../components/FancyTable";
import "../csss/SearchCandidates.css";
import logo from '../img/logo_softlink.png';
import axios, {AxiosResponse} from "axios";

interface Props {
}

interface IEntry {
    name: string;
    url: string;
}

interface IData {
    data: IEntry[];
}

const SearchCandidates: React.FC<Props> = () => {
    const navigate = useNavigate();
    const redirectHome = () => {
        let path= '/';
        navigate(path);
    }

    const [jobTitle, setJobTitle] = React.useState("");
    let lst:string[] = [];
    const [skills, setSkills] = React.useState(lst);
    const [location, setLocation] = React.useState("");
    const [r, setR] = React.useState(false);
    let d: IData;
    const [entries, setEntries] = React.useState(d);

    const searchCandidates = () => {
        axios.get("/api/search-candidates", {
            params: {
                job_title: jobTitle,
                skills_list: skills,
                location: location,
            }})
            .then((res: AxiosResponse<IData>) => {
                setEntries(res.data);
                setR(true);})
            .catch((err) => console.log(err));
    };

    const onChangeJobTitle = (event: React.ChangeEvent<HTMLInputElement>) => {
        setJobTitle(event.target.value);
    };
    const onChangeLocation = (event: React.ChangeEvent<HTMLInputElement>) => {
        setLocation(event.target.value);
    };


    return (
        <div >
            <div className="container cntr">
                <img className="logo" src={logo} alt="Logo" onClick={redirectHome}/>
            </div>
            <div className="divStyle">
                <div className="margin_box">
                    <div className="titles">
                        Job title:
                    </div>
                    <div className="go309598777">
                        <input className="go3450369076" type="tex" onChange={onChangeJobTitle} placeholder="Enter job title" />
                    </div>
                </div>
                <br />
                <div className="margin_box skills_box">
                    <div className="titles">
                        Skills:
                    </div>
                    <TagsInput
                        value={skills}
                        onChange={setSkills}
                        name="Skills"
                        placeHolder="Type and press enter"
                    />
                </div>
                <br />
                <div className="margin_box">
                    <div className="titles">
                        Location:
                    </div>
                    <div className="go309598777">
                        <input className="go3450369076" type="tex" onChange={onChangeLocation} placeholder="Enter location" />
                    </div>
                </div>
                <button className="button_img" onClick={searchCandidates}>Search</button>
            </div>
            { r &&
                <div className="divStyleTable">
                    <FancyTable entries={entries}/>
                </div>
            }
        </div>
    );
}

export default SearchCandidates;