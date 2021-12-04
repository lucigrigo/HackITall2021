import * as React from "react";

interface Props {
}

const SearchCandidates: React.FC<Props> = () => {
    return (
        <div>
            <div >Stack Exchange Search</div>
            <div>
                <p>This will search Stack Exchange questions for given title text.</p>
                <p>
                    Enter your search text and click the icon or press the Enter key. A
                    list of matching questions will be shown.
                </p>
                <p>After that, you can click on a question to see the answers.</p>
                <p>
                    Full source available at{" "}
                    <a href="https://github.com/reactjsexample/react-typescript-example">
                        https://github.com/reactjsexample/react-typescript-example
                    </a>
                </p>
                <h3>Written in React 16.9.0 with TypeScript</h3>
                <h4>By JC Lango</h4>
            </div>
        </div>
    );
}

export default SearchCandidates;