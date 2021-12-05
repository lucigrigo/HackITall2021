import * as React from "react";
import background from "../img/background.jpg";
import { TagsInput } from "react-tag-input-component";
import "../csss/SearchCandidates.css";

interface Props {
}

const divStyle = {
    height: '100%',
    margin: 0,
    backgroundImage: `url(${background})`,
    backgroundSize: 'cover'
};

const SearchCandidates: React.FC<Props> = () => {
    const jobTitles = [
        "Software engineer",
        "DevOps",
        "Software developer",
        "Site reliability engineer",
        "Business analyst",
    ];

    const [jobTitle, setJobTitle] = React.useState("");
    const [skills, setSkills] = React.useState(["example"]);
    const [location, setLocation] = React.useState("");
    const [r, setR] = React.useState(false);

    const searchCandidates = () => {
        // Request la API
        setR(true);
    }

    const onChangeJobTitle = (event: React.ChangeEvent<HTMLInputElement>) => {
        setJobTitle(event.target.value);
    };
    const onChangeLocation = (event: React.ChangeEvent<HTMLInputElement>) => {
        setLocation(event.target.value);
    };


    return (
        <div style={divStyle}>
            <div>
                <div className="col-xs-12 col-sm-7 example-col">
                    Job Title:
                    <br />
                    <input type="tex" onChange={onChangeJobTitle} />
                </div>
                <br />
                <div>
                    Skills:
                    <br />
                    <TagsInput
                        value={skills}
                        onChange={setSkills}
                        name="Skills"
                        placeHolder="Type and press enter"
                    />
                </div>
                <br />
                <div>
                    Location:
                    <br />
                    <input type="tex" onChange={onChangeLocation} />
                </div>
                <button><img src="../img/search.jpg" onClick={searchCandidates}  alt="search"/></button>
            </div>
            { r &&
                <div>
                    Aici afisam userii
                </div>
            }
        </div>
    );
}

export default SearchCandidates;