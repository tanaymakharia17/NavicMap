import React from 'react';

const Select = ({ name, label, value, onChange, options, error }) => {
    return (
        <div className="form-group">
            <label htmlFor={name}
                className="form-label">
                {label}
            </label>

            <select id={name}
                value={value}
                className="form-control"
                onChange={onChange}>
                <option value="" />
                {options.map(option => (
                    <option key={option._id}
                        value={option.type}
                        disabled={!option.count}>
                        {option.type}
                    </option>
                ))}
            </select>

            {error && <div className="alert alert-danger">{error}</div>}
        </div>
    );
}

export default Select;