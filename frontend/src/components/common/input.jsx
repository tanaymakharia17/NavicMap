import React from 'react';

const Input = ({ name, type, value, label, options, onChange, onClick }) => {
    return (
        <div className="form-group" style={{ background: "white", borderRadius: "5px" }}>
            <input id={name}
                value={value}
                onChange={onChange}
                type={type}
                placeholder={label}
                size={35}
                className="form-control"
                style={{ border: "none" }}>
            </input>

            <div id={name} className="mx-3 p-1" style={{ listStyle: "none" }}>
                {options[name].map(
                    option => (
                        <li id={name}
                            key={option}
                            className="list"
                            style={{ cursor: "pointer" }}
                            onClick={onClick}>
                            {option}
                        </li>
                    )
                )}
            </div>
        </div>
    );
}

export default Input;